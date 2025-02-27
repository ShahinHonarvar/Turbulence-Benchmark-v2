def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def extract_letters(sub):
        return ''.join((c for c in sub if c.isalpha()))
    s = s[:301]
    palindromes = set()
    length_range = range(50, 61)
    for length in length_range:
        for i in range(len(s) - length + 1):
            sub = extract_letters(s[i:i + length])
            if len(sub) == length and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes