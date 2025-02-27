from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for start in range(4, 8):
        for end in range(start, 8 + 1):
            substring = s[start:end + 1].lower()
            if english_letters.issuperset(substring):
                if len(substring) >= 5:
                    palindromes.add(substring)
    return palindromes