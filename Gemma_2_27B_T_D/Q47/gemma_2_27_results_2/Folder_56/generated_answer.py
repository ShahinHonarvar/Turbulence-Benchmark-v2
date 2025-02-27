def palindromes_of_specific_lengths(text):
    substring = text[1:10]
    palindromes = set()
    for i in range(len(substring) - 2):
        for j in range(i + 3, min(i + 8, len(substring)) + 1):
            palindrome_candidate = substring[i:j].lower()
            if palindrome_candidate == palindrome_candidate[::-1] and palindrome_candidate.isalpha():
                palindromes.add(palindrome_candidate)
    return palindromes