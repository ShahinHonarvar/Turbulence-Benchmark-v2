from itertools import permutations
    from collections import Counter
    from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]

    def make_palindrome(char_counts, length, palindrome):
        if length == 0:
            return {palindrome} if len(palindrome) >= 6 else set()
        for char in char_counts:
            if char_counts[char] > 0:
                char_counts[char] -= 1
                palindrome += char
                palindromes = make_palindrome(char_counts, length - 1, palindrome)
                if palindromes:
                    return palindromes
                palindrome = palindrome[:-1]
                char_counts[char] += 1
        return set()
    s = ''.join(filter(str.isalpha, s[1:7])).lower()
    s_counter = Counter(s)
    palindromes = set()
    for chars_permutation in permutations(s_counter, sum(s_counter.values())):
        palindrome = ''.join(chars_permutation)
        if is_palindrome(palindrome):
            palindromes.add(palindrome)
    if len(palindromes) == 0:
        palindromes = make_palindrome(s_counter, sum(s_counter.values()), '')
    return palindromes