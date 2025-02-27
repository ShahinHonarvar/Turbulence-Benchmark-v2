def palindrome_of_length_at_least_n(str):
    low, high = (0, len(str) - 1)
    palindrome_set = set()
    str = str.lower()
    while low + 2 <= high:
        if str[low] == str[high]:
            palindrome_set.add(str[low:high + 1])
        low += 1
        high -= 1
    return palindrome_set