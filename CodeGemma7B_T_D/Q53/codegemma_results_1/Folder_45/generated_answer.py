def palindrome_of_length_at_least_n(text):
    palindrome_set = set()
    text = text.lower()
    palindromes = []
    for i in range(len(palindromes)):
        if i < len(palindromes) - 46:
            if text[i] == text[i + 1] and text[i] == text[i + 2] and (text[i] == text[i + 3]) and (text[i] == text[i + 4]) and (text[i] == text[i + 5]) and (text[i] == text[i + 6]) and (text[i] == text[i + 7]) and (text[i] == text[i + 8]) and (text[i] == text[i + 9]) and (text[i] == text[i + 10]) and (text[i] == text[i + 11]) and (text[i] == text[i + 12]) and (text[i] == text[i + 13]) and (text[i] == text[i + 14]) and (text[i] == text[i + 15]) and (text[i] == text[i + 16]) and (text[i] == text[i + 17]) and (text[i] == text[i + 18]) and (text[i] == text[i + 19]) and (text[i] == text[i + 20]) and (text[i] == text[i + 21]) and (text[i] == text[i + 22]) and (text[i] == text[i + 23]) and (text[i] == text[i + 24]) and (text[i] == text[i + 25]) and (text[i] == text[i + 26]) and (text[i] == text[i + 27]) and (text[i] == text[i + 28]) and (text[i] == text[i + 29]) and (text[i] == text[i + 30]) and (text[i] == text[i + 31]) and (text[i] == text[i + 32]) and (text[i] == text[i + 33]) and (text[i] == text[i + 34]) and (text[i] == text[i + 35]) and (text[i] == text[i + 36]) and (text[i] == text[i + 37]) and (text[i] == text[i + 38]) and (text[i] == text[i + 39]) and (text[i] == text[i + 40]) and (text[i] == text[i + 41]) and (text[i] == text[i + 42]) and (text[i] == text[i + 43]) and (text[i] == text[i + 44]) and (text[i] == text[i + 45]) and (text[i] == text[i + 46]):
                palindromes.append(text[i:i + 47])
    for palindrome in palindromes:
        palindrome_set.add(palindrome)
    return palindrome_set