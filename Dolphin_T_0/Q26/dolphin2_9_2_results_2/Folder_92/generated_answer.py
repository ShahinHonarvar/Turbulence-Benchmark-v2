def sum_in_range(docs):
    result = 0
    for num in docs:
        if 5 <= num <= 9:
            result += num
    return result if result else 0