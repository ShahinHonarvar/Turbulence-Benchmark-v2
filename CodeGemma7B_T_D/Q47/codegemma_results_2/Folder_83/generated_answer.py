def palindromes_of_specific_lengths(text):
    text = text.lower()
    selected_text = text[75:96]
    palindromes = set()
    for i in range(len(selected_text)):
        for j in range(i + 7, min(i + 10, len(selected_text))):
            if selected_text[i] == selected_text[j]:
                palindrome = selected_text[i:j + 1]
                if palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes