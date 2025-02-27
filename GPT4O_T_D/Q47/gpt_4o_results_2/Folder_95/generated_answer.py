def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]

    def extract_letters(text):
        return ''.join(filter(str.isalpha, text))
    palindromes = set()
    substring = s[12:57].lower()
    letters_only = extract_letters(substring)
    for start in range(len(letters_only)):
        for length in range(20, 22):
            if start + length > len(letters_only):
                break
            candidate = letters_only[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes