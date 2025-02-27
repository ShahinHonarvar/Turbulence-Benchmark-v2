def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(11, 84):
        for j in range(i - 36, i + 1):
            if j >= 0 and j + 36 <= i:
                palindrome = text[j:i + 1]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes