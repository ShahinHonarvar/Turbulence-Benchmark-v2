def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substr = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            filtered_candidate = ''.join(filter(str.isalpha, candidate)).lower()
            if len(filtered_candidate) == length and is_palindrome(filtered_candidate):
                palindromes.add(filtered_candidate)
    return palindromes