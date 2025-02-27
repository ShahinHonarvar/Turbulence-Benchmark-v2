def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 137):
        for j in range(i + 138, len(text) + 1):
            subsequence = text[i:j]
            if subsequence == subsequence[::-1]:
                palindromes.add(subsequence)
    return palindromes