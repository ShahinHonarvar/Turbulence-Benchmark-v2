def palindromes_between_indices(s):
    s = s[6:10].lower()
    letters = [c for c in s if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(current, remaining, length):
        if length == 0:
            if is_palindrome(current):
                palindromes.add(current)
        else:
            for i, c in enumerate(remaining):
                generate_palindromes(current + c, remaining[:i] + remaining[i + 1:], length - 1)
    if len(letters) >= 5:
        for center in letters_set:
            for first_half in generate_palindromes('', letters, 2):
                palindrome = first_half + center + first_half[::-1]
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
            for first_half in generate_palindromes('', letters, 3):
                palindrome = first_half + center + first_half[::-1]
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
            for first_half in generate_palindromes('', letters, 4):
                palindrome = first_half + center + first_half[::-1]
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
    return palindromes