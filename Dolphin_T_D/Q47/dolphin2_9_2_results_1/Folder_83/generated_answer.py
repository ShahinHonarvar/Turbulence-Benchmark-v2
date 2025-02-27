def palindromes_of_specific_lengths(input_string):
    substring = input_string[75:96]
    length = len(substring)
    palindromes_set = set()
    for i in range(length):
        for j in range(i + 7, length + 1):
            current_string = substring[i:j]
            if all((c.isalpha() for c in current_string)):
                lower_string = current_string.lower()
                if lower_string == lower_string[::-1] and 7 <= len(lower_string) <= 9:
                    palindromes_set.add(current_string)
    return palindromes_set