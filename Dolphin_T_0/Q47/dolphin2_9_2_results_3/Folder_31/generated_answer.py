def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    relevant_substring = s[11:84]
    relevant_palindromes = [relevant_substring[i:j] for i in range(len(relevant_substring)) for j in range(i + 36, len(relevant_substring) + 1)]
    filtered_palindromes = [p for p in relevant_palindromes if is_palindrome(p) and 37 <= len(p) <= 60]
    return set(filtered_palindromes)