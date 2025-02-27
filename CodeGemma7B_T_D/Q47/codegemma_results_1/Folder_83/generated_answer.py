def palindromes_of_specific_lengths(text):
    specific_area_string = text[74:96]
    specific_area_string = specific_area_string.lower()
    palindromes = set()
    for i in range(len(specific_area_string)):
        for j in range(i + 7, min(i + 10, len(specific_area_string))):
            if specific_area_string[i] == specific_area_string[j]:
                palindrome = specific_area_string[i:j + 1]
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes