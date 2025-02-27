from collections import defaultdict

def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, min(5, len(s))):
        substring = s[i:5]
        letters = set((c.lower() for c in substring if c.lower() in english_letters))
        if len(letters) >= 2:
            for j in range(1, 2 ** len(letters)):
                selected_letters = [letter for k, letter in enumerate(letters) if j & 1 << k != 0]
                if len(selected_letters) < 2:
                    continue
                palindrome = selected_letters[0] + ''.join(selected_letters[1:-1]) + selected_letters[-1]
                if j & j << 1 == 0:
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
                elif len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes