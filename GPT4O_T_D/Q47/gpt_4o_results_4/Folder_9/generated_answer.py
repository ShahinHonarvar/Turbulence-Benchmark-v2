def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def extract_letters(text):
        return ''.join([char for char in text if char.isalpha()])
    palindromes = set()
    sub_s = s[:301].lower()
    for start in range(len(sub_s)):
        for length in range(50, 61):
            end = start + length
            if end > len(sub_s):
                break
            candidate = extract_letters(sub_s[start:end])
            if len(candidate) == length and is_palindrome(candidate):
                palindromes.add(sub_s[start:end])
    return palindromes