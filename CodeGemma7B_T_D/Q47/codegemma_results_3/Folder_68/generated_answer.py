def palindromes_of_specific_lengths(text):
    case_insensitive_text = text.lower()
    specified_range = case_insensitive_text[0:51]
    specified_range_palindromes = set()
    for i in range(len(specified_range)):
        for j in range(i + 1, min(i + 101, len(specified_range))):
            substring = specified_range[i:j]
            if substring == substring[::-1] and len(substring) >= 50 and (len(substring) <= 100):
                specified_range_palindromes.add(substring)
    return specified_range_palindromes