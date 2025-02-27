def palindrome_of_length_at_least_n(str):
    """
    >>> palindrome_of_length_at_least_n('Anna')
    {'anna'}
    >>> palindrome_of_length_at_least_n('Bob')
    set()
    >>> palindrome_of_length_at_least_n('madam')
    {'madam', 'ada'}
    """
    layer = []
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i:j + 1] == str[i:j + 1][::-1] and 47 <= j - i + 1 <= 100:
                layer.append(str[i:j + 1])
    return set(layer)