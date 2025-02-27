def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[11:94]
    palindrome_set = set()
    for x in range(0, len(text)):
        for y in range(34, 55):
            if text[x:x + y] == text[x:x + y][::-1]:
                palindrome_set.add(text[x:x + y])
    return palindrome_set