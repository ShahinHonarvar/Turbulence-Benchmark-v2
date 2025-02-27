from collections import defaultdict

def palindrome_of_length_n(str):
    palindromes = defaultdict(set)
    str = str.lower()
    for i in range(len(str)):
        for j in range(i + 475, len(str) + 1):
            if str[i] in ('a', 'e', 'i', 'o', 'u') and str[j - 1] in ('a', 'e', 'i', 'o', 'u'):
                palindrome = str[i:j]
                palindromes[palindrome].add((i, j - 1))
    return set(palindromes.keys())