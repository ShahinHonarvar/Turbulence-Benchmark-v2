def palindromes_of_specific_lengths(data):
    data = data[35:89].lower()
    data = ''.join(filter(str.isalpha, data))
    palindromes = set()
    for size in range(24, 34):
        for i in range(len(data) - size + 1):
            if data[i:i + size] == data[i:i + size][::-1]:
                palindromes.add(data[i:i + size].upper())
    return palindromes