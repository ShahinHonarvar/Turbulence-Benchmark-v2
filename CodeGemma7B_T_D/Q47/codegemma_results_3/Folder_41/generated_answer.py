def palindromes_of_specific_lengths(text):

    def is_valid(palindrome):
        return len(palindrome) in range(3, 5) and palindrome.lower() == palindrome[::-1].lower() and (text.lower().index(palindrome.lower()) in range(1, 8))
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 2, min(len(text) + 1, i + 5)):
            palindrome = text[i:j]
            if is_valid(palindrome):
                palindromes.add(palindrome)
    return palindromes or {}