from collections import defaultdict

def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(101, 293):
        for j in range(i, i + 182):
            if j <= len(s) and all((s[k].lower() in english_letters for k in range(i, j + 1))):
                if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                    palindromes.add(s[i:j + 1])
    return palindromes