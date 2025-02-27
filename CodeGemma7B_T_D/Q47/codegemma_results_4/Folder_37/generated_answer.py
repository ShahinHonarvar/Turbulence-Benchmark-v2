def palindromes_of_specific_lengths(txt):
    char = re.sub('[^a-zA-Z]', '', txt)
    palindromes = set()
    for i in range(len(char) - 2):
        for j in range(i + 3, min(len(char), i + 6)):
            if char[i] == char[j]:
                result = char[i:j + 1]
                if result == result[::-1]:
                    palindromes.add(result)
    return palindromes