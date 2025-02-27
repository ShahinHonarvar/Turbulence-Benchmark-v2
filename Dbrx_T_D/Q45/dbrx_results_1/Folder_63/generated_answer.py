from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, min(i + 4, len(s))):
            substring = s[i:j + 1]
            letters = set((c for c in substring if c.lower() in eng_letters))
            if len(letters) < 2:
                continue
            for arrangement in itertools.product(letters, repeat=2):
                palindrome = ''.join(arrangement * (len(substring) // 2)) + ''.join(substring[len(substring) // 2:])
                if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes