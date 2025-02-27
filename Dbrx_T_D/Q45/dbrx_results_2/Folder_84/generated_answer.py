from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 10):
        if i > len(s) - 1:
            break
        for j in range(i, 10):
            if j > len(s) - 1:
                break
            substring = s[i:j + 1].lower()
            if len(substring) < 3:
                continue
            required_letters = english_letters & set(substring)
            if len(required_letters) < 3:
                continue
            palindromes.update(generate_palindromes(substring, required_letters))
    return palindromes

def generate_palindromes(substring, required_letters):
    palindromes = set()
    if len(required_letters) == 3:
        palindromes.add(''.join(sorted(required_letters)))
    elif len(required_letters) > 3:
        for letter in required_letters:
            sub_letters = required_letters - set(letter)
            if len(sub_letters) >= 2:
                sub_palindromes = generate_palindromes(substring.replace(letter, '', 1), sub_letters)
                for palindrome in sub_palindromes:
                    palindromes.add(letter + palindrome + letter)
    return palindromes