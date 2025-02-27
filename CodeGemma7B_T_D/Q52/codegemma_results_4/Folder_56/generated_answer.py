def palindrome_of_length_n(str):
    arr = list(str.lower())
    result = set()
    for i in range(len(arr) - 94):
        temp = arr[i:i + 95]
        temp.extend(temp[::-1])
        if ''.join(temp) in str.lower():
            result.add(''.join(temp))
    if len(result) == 0:
        return 'There is no palindrome of that length.'
    return result