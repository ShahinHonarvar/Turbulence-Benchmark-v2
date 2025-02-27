from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 9):
        for j in range(i, 9):
            substr = s[i:j + 1].lower()
            if all((char in english_letters for char in substr)) and len(substr) >= 4:
                chars = defaultdict(int, {'': 0, **{char: 1 for char in set(substr)}})
                can_be_palindrome = True
                for char in substr:
                    chars[char] += 1
                    if chars[char] > 1:
                        can_be_palindrome = False
                        break
                if can_be_palindrome:
                    palindromes.add(''.join(sorted(substr)))
    return palindromes