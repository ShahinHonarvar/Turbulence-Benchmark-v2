def palindromes_between_indices(s):
    English_letters = set(s[1:8].lower())
    if len(English_letters) < 3:
        return set()
    palindromes = set()
    for length_palindrome in range(3, len(s[1:8]) + 1):
        for start_idx in range(0, len(s[1:8]) - length_palindrome + 1):
            palindrome = s[1:8][start_idx:start_idx + length_palindrome]
            palindrome_reversed = palindrome[::-1]
            if set(palindrome.lower()) <= English_letters and set(palindrome_reversed.lower()) <= English_letters and (palindrome == palindrome_reversed):
                palindromes.add(palindrome)
    return palindromes