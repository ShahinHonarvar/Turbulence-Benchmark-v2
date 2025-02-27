def palindromes_of_specific_lengths(input_str):
    substring = input_str[100:301]
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub.lower() or sub == sub.upper():
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes