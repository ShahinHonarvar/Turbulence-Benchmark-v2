def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 97):
        for length in range(45, 53):
            if i + length <= len(s):
                palindrome_candidate = s[i:i + length].lower()
                if palindrome_candidate == palindrome_candidate[::-1]:
                    if palindrome_candidate.isalpha():
                        palindromes.add(palindrome_candidate)
    return palindromes