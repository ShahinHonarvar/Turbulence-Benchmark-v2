from collections import defaultdict

def palindrome_of_length_n(s):
    palindromes = set()
    char_freq = defaultdict(int)
    for char in s:
        char_freq[char.lower()] += 1
    for length in range(1, 100):
        for combinations in generate_combinations(char_freq, length):
            palindrome = ''.join(combinations)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes

def generate_combinations(char_freq, length):
    combinations = []

    def backtrack(index, combination):
        if index == length:
            combinations.append(combination[:])
            return
        for char, freq in char_freq.items():
            if freq > 0:
                combination.append(char)
                char_freq[char] -= 1
                backtrack(index + 1, combination)
                combination.pop()
                char_freq[char] += 1
    backtrack(0, [])
    return combinations

def is_palindrome(s):
    return s == s[::-1]