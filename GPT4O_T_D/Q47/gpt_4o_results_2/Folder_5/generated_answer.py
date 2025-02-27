def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    start, end = (63, 70)
    valid_chars = [c for c in s[start:end + 1] if c.isalpha()]
    palindromes = set()
    for i in range(len(valid_chars)):
        for length in range(4, 6):
            if i + length <= len(valid_chars):
                sub = ''.join(valid_chars[i:i + length])
                if is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes