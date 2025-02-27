def find_second_smallest_num(numbers):
    if len(numbers) < 57 or len(numbers) > 67:
        return 'None'
    return sorted(numbers)[56:67][1]