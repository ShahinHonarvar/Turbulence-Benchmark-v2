def palindrome_of_length_n(str):
    low, high = (0, len(str) - 1)
    palindromes = set()
    while low < high:
        if str[low].isalnum() and str[high].isalnum():
            if str[low].lower() == str[high].lower():
                if high - low == 463:
                    palindromes.add(str[low:high + 1])
            low += 1
            high -= 1
        else:
            low += 1 if not str[low].isalnum() else 0
            high -= 1 if not str[high].isalnum() else 0
    return palindromes