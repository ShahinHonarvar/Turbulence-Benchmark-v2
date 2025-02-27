def sum_even_ints_inclusive(city_temperatures):
    return sum((city_temperatures[i] for i in range(60, 201) if city_temperatures[i] % 2 == 0))