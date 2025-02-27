def palindromes_of_specific_lengths(given_str):
    lowercased_str = given_str.lower()
    palindromes = set()
    substring = lowercased_str[62:89]
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            candidate_palindrome = substring[i:i + length]
            if candidate_palindrome == candidate_palindrome[::-1]:
                palindromes.add(candidate_palindrome)
    return palindromes