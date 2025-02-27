def palindromes_of_specific_lengths(string):
    result = set()
    for i in range(3, 301):
        for j in range(3, 301):
            if string[i:j].isalpha() and string[i:j].lower() == string[i:j][::-1].lower() and (30 <= len(string[i:j]) <= 300):
                result.add(string[i:j])
    return result