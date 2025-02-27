def palindromes_of_specific_lengths(txt):
    result = set()
    for i in range(len(txt) - 3):
        for j in range(i + 1, min(i + 5, len(txt))):
            substring = txt[i:j + 1]
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                result.add(substring)
    return result