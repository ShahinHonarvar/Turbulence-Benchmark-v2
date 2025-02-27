from collections import defaultdict

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()

    def find_palindromes(s):
        palindromes = defaultdict(list)
        for i in range(len(s) - 5):
            for j in range(i + 3, i + 9):
                if j <= len(s) and is_palindrome(s[i:j]):
                    palindromes[len(s[i:j])].append(s[i:j])
        return palindromes
    s = s[10:75]
    palindromes = find_palindromes(s)
    result = set()
    for i in range(6, 9):
        result.update(palindromes[i])
    return result