from itertools import combinations

def palindrome_of_length_at_least_n(s: str) -> set:
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    palindromes = set()
    for i in range(91, len(s) + 1):
        substrings = (''.join(s[j:j + n]) for n in range(i, 0, -1) for j in range(0, len(s) - n + 1))
        for substring in substrings:
            if substring == substring[::-1]:
                substring = substring.lower()
                if all((letter in letters for letter in substring)):
                    palindromes.add(substring)
    return palindromes