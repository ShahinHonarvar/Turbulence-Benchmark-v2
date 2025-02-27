def palindromes_of_specific_lengths(s):
    substr = s[45:99]
    filtered_substr = ''.join((c for c in substr if c.isalpha())).lower()
    palindromes = set()
    length_range = range(40, 48)
    for length in length_range:
        for i in range(len(filtered_substr) - length + 1):
            potential_palindrome = filtered_substr[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes