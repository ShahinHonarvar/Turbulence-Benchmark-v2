def palindromes_of_specific_lengths(txt):
    results = set()
    for i in range(0, len(txt) - 2):
        for j in range(i + 3, 6):
            palindrome = txt[i:j]
            if palindrome.lower() == palindrome[::-1].lower() and palindrome.isalpha():
                results.add(palindrome)
    return results