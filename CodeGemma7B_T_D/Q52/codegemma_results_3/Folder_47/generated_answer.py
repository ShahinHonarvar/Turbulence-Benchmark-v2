def palindrome_of_length_n(str):
    low = str.lower()
    low = low.replace(' ', '')
    low = low.replace('.', '')
    palindrome = set()
    for i in range(len(low)):
        for j in range(i + 1, len(low)):
            for k in range(j + 1, len(low)):
                if low[i] == low[j] and low[j] == low[k]:
                    palindrome.add(low[i:k + 1])
    return palindrome