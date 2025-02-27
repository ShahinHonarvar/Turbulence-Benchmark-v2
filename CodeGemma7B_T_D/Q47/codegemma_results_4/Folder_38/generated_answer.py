def palindromes_of_specific_lengths(text):
    sub_text = text[17:88]
    palindromes = set()
    for i in range(len(sub_text)):
        for j in range(i, len(sub_text)):
            palindrome = sub_text[i:j + 1].lower()
            if len(palindrome) >= 38 and len(palindrome) <= 60:
                palindromes.add(palindrome)
    return palindromes