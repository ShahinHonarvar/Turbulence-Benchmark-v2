def palindromes_of_specific_lengths(text):
    three_eight_to_forty_nine_letters = set()
    for i in range(28, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            substring_lower = substring.lower()
            if substring_lower == substring_lower[::-1] and len(substring) >= 38 and (len(substring) <= 49):
                three_eight_to_forty_nine_letters.add(substring)
    return three_eight_to_forty_nine_letters