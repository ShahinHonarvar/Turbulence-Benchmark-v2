from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    char_freq = defaultdict(int)
    for char in string.lower():
        if char.isalpha():
            char_freq[char] += 1
    result = set()
    for i in range(len(string)):
        for j in range(i + 48, len(string)):
            palindrome = string[i:j + 1]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result