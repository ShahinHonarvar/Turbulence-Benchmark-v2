def palindromes_of_specific_lengths(str):
    result = set()
    for i in range(len(str)):
        for j in range(i + 3, min(i + 8, len(str))):
            temp = str[i:j + 1]
            if temp == temp[::-1] and temp.lower() in str[i:j + 1].lower():
                result.add(temp)
    return result