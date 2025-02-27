from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) == 4 and substring == substring[::-1]:
                    palindromes.add(substring)
                elif len(substring) > 4:
                    freq = defaultdict(int)
                    for char in substring:
                        freq[char] += 1
                    odd_count = sum((freq[char] % 2 for char in english_letters))
                    if odd_count <= 1:
                        palindromes.add(substring)
    return palindromes