def palindromes_of_specific_lengths(string):
    lengths = set()
    for i in range(10, 76):
        for j in range(i + 2, 76):
            substring = string[i:j]
            if set([char for char in substring if char.isalpha()]).issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}) and len(substring) in range(10, 21):
                if substring.lower() == substring[::-1].lower() and substring not in lengths:
                    lengths.add(substring)
    if not lengths:
        return
    else:
        return lengths