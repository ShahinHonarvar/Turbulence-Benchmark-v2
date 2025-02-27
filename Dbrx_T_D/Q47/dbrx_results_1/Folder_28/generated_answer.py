def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 72):
        for j in range(21, 33):
            if i + j - 1 < len(s):
                palindrome_candidate = s[i:i + j].lower()
                if palindrome_candidate == palindrome_candidate[::-1] and palindrome_candidate.isalpha():
                    palindromes.add(palindrome_candidate)
    return palindromes