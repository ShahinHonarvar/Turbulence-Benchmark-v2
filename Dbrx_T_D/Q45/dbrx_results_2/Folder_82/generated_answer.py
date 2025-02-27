from string import ascii_lowercase
    from itertools import product

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    english_letters = set(ascii_lowercase)
    for i in range(1, 6):
        for j in range(i, 7):
            substring = s[i:j + 1]
            substring = ''.join(filter(english_letters.__contains__, substring)).lower()
            if len(substring) >= 7:
                product_iter = product(substring, repeat=int(len(substring) / 2))
                for p in product_iter:
                    palindrome = ''.join(p)
                    if len(palindrome) > 7 and is_palindrome(palindrome) and (palindrome not in palindromes):
                        palindromes.add(palindrome)
    return palindromes