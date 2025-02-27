def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    clean_substring = ''.join(filter(str.isalpha, s[10:76]))
    palindromes_set = set()
    for start in range(len(clean_substring)):
        for length in range(10, 21):
            end = start + length
            if end <= len(clean_substring):
                if is_palindrome(clean_substring[start:end]):
                    palindromes_set.add(clean_substring[start:end])
    return palindromes_set